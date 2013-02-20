from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget

Builder.load_file( "kivyextras.kv" )

class ColorChooser( Widget ) :
 
    sldr = ObjectProperty( None )
    sldg = ObjectProperty( None )
    sldb = ObjectProperty( None )
    label = StringProperty( "Pick up a color :" )

    def __init__( self, label, rgb, **kargs ) : 
        super( ColorChooser, self ).__init__( **kargs )
        self.label = label
        self.sldr.value_normalized = rgb[0]
        self.sldg.value_normalized = rgb[1]
        self.sldb.value_normalized = rgb[2]

    def rgb( self ) : 
        return self.sldr.value_normalized, \
               self.sldg.value_normalized, \
               self.sldb.value_normalized
