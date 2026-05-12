import yaml

class EchoInstrument:
    def __init__(self, filename):
      self.filename = filename
      self.channels = self.load_data() 
    
    def load_data(self):
       with open(self.filename, 'r') as f:
          data = yaml.safe_load(f)

       return data['channels']
    
    def get_channel(self, frequency):
       for channel in self.channels:
          if channel['frequency'] == frequency:
             return channel
          
       raise ValueError(f'No channel found for frequency {frequency} GHz')
    
    def get_frequencies(self):
       return [channel['frequency'] for channel in self.channels]
    
    def get_beam_fwhm(self, frequency):
       channel = self.get_channel(frequency)
       return channel['beam_fwhm']
    
    def get_polarization_sensitivity(self, frequency):
       channel = self.get_channel(frequency)
       return channel['polarization_sensitivity']