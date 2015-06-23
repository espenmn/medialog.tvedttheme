from zope.interface import implements, Interface, Attribute
from Products.Five import BrowserView

#from plone.dexterity.utils import iterSchemata
from zope.schema import getFields
from plone.dexterity.interfaces import IDexterityContent


 
    
class IProductsView(Interface):
    """
   view interface
    """

        
    def test():
        """ test method"""
 

 

class ProductsView(BrowserView):
    """
   browser view
    """

    def test(self):
        """
        test method
        """
        
        dummy = _(u'a dummy string')
        return {'dummy': dummy}


    @property
    def rtfields(self):
        richtext_fields = []
        context=self.context
        if IDexterityContent.providedBy(context):
            for schemata in iterSchemata(context):
                for name, field in getFields(schemata).items():
                    #checking for rich text field
                    #if isinstance(field, RichText):
                    if str(field.__class__) == "<class 'plone.app.textfield.RichText'>":
                        richtext_fields.append(name)
        return richtext_fields

