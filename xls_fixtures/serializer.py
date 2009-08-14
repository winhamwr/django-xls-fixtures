import xlrd

from django.conf import settings
from django.core.serializers import base, python as python_serializer
from django.db import models
from django.utils.encoding import smart_unicode, is_protected_type

LABEL_FIELD = 300

"""
Excel fixtures are formatted with a header row containing the field names and
then one or more rows representing model instances. The model name is the name
of worksheet. One excel workbook can have any number of sheets.
"""
#objects = serializers.deserialize(format, fixture)
#for obj in objects:
    #objects_in_fixture += 1
    #models.add(obj.object.__class__)
    #obj.save()
#object_count += objects_in_fixture

class Deserializer(base.Deserializer):
    """
    Deserialize xls. Uses django.core.serializers.xml_serializer as a guide.
    """

    def __init__(self, stream_or_string, **options):
        """
        Create the xlrd book from our stream and set up the first sheet for
        deserialization.
        """
        super(Deserializer, self).__init__(stream_or_string, **options)
        self.book = xlrd.open_workbook(file_contents=self.stream)

        self.cur_sheet_index = 0
        self.cur_sheet = self.book.sheet_by_index(self.cur_sheet_index)
        self.cur_model = self._get_model_from_sheet(self.cur_sheet)

        self.cur_row_index = 0
        self.row_field_map = self._set_fields_for_row(
            self.cur_sheet.row(self.cur_row_index))

    def _set_fields_for_row(self, row):
        """
        Set up the field mappings for the given row
        """
        label_cell = row.pop(0)
        mapping = []

        # Get the field type from the model for each cell
        for index, cell in enumerate(row):
            if index == 0: # Label field
                mapping.append(LABEL_FIELD)
            else:
                # Each cell should just contain text
                assert cell.ctype == xlrd.Cell.XL_CELL_TEXT
                field_type = self.cur_model._meta.get_field(cell)
                mapping.append(field_type)

        return mapping

    def _get_model_from_sheet(self, sheet):
        """
        Get the model name for the given sheet. Handles parsing out the comments
        """
        # The model name is the section before the first space (if there is one)
        model_name = sheet.name.split(' ')[0]
        return python_serializer._get_model(model_name)

    def next(self):
        next_row = self.cur_sheet.row(self.cur_row_index)
        if new_row:
            obj = self._handle_row(new_row)
            self.cur_row_index += 1
            return obj
        else: # End of sheet
            self.cur_sheet_index += 1
            if self.cur_sheet_index < self.book.nsheets:
                self.cur_sheet = self.book.sheet_by_index(self.cur_sheet_index)
                self.cur_row_index = 0
                self.next()
            else:
                raise StopIteration

    def _handle_row(self, row):
        """
        Convert a a row of cells to a Djano ORM object.
        """
        pass
        ## Look up the model using the model loading mechanism. If this fails,
        ## bail.
        #Model = self._get_model_from_node(node, "model")

        ## Start building a data dictionary from the object.  If the node is
        ## missing the pk attribute, bail.
        #pk = node.getAttribute("pk")
        #if not pk:
            #raise base.DeserializationError("<object> node is missing the 'pk' attribute")

        #data = {Model._meta.pk.attname : Model._meta.pk.to_python(pk)}

        ## Also start building a dict of m2m data (this is saved as
        ## {m2m_accessor_attribute : [list_of_related_objects]})
        #m2m_data = {}

        ## Deseralize each field.
        #for field_node in node.getElementsByTagName("field"):
            ## If the field is missing the name attribute, bail (are you
            ## sensing a pattern here?)
            #field_name = field_node.getAttribute("name")
            #if not field_name:
                #raise base.DeserializationError("<field> node is missing the 'name' attribute")

            ## Get the field from the Model. This will raise a
            ## FieldDoesNotExist if, well, the field doesn't exist, which will
            ## be propagated correctly.
            #field = Model._meta.get_field(field_name)

            ## As is usually the case, relation fields get the special treatment.
            #if field.rel and isinstance(field.rel, models.ManyToManyRel):
                #m2m_data[field.name] = self._handle_m2m_field_node(field_node, field)
            #elif field.rel and isinstance(field.rel, models.ManyToOneRel):
                #data[field.attname] = self._handle_fk_field_node(field_node, field)
            #else:
                #if field_node.getElementsByTagName('None'):
                    #value = None
                #else:
                    #value = field.to_python(getInnerText(field_node).strip())
                #data[field.name] = value

        ## Return a DeserializedObject so that the m2m data has a place to live.
        #return base.DeserializedObject(Model(**data), m2m_data)

    #def _handle_fk_field_node(self, node, field):
        #"""
        #Handle a <field> node for a ForeignKey
        #"""
        ## Check if there is a child node named 'None', returning None if so.
        #if node.getElementsByTagName('None'):
            #return None
        #else:
            #return field.rel.to._meta.get_field(field.rel.field_name).to_python(
                       #getInnerText(node).strip())

    #def _handle_m2m_field_node(self, node, field):
        #"""
        #Handle a <field> node for a ManyToManyField.
        #"""
        #return [field.rel.to._meta.pk.to_python(
                    #c.getAttribute("pk"))
                    #for c in node.getElementsByTagName("object")]