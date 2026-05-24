"""Utilities for the echosims package: loads the ECHO instrument configuration."""

# import libraries
from importlib import resources
from pathlib import Path
import yaml

# internal function for guessing the paths of data/echo.yaml
def _candidate_paths(filename):
   """Yield candidate paths for filename, in priority order."""
   # When data folder is inside echosims while packaging as _data,
   # obtain the location of echosims (resources.files("echosims")) and build the path <wherever echosims lives>/echosims/_data/echo.yaml,
   # return the path as the first guess
   packaged = resources.files("echosims") / "_data" / filename
   yield Path(packaged) 

   # When data folder is not inside echosims,
   # obtain the absolute path of utils.py (Path(__file__).resolve()), move two levels up and obtain the path to repo root,
   # return <path to repo root>/data/echo.yaml as the second guess
   repo_root = Path(__file__).resolve().parent.parent
   yield repo_root / "data" / filename 


def _resolve(filename):
   """Return the first existing path from _candidate_paths(filename)."""
   for candidate in _candidate_paths(filename):
      if candidate.exists():
         return candidate
   raise FileNotFoundError(f"Could not find {filename} in any known location")


class EchoInstrument:
    """Represents the ECHO instrument and its frequency channels."""

    def __init__(self):
      self.channels = self.load_data() 
    
    def load_data(self):
       path = _resolve("echo.yaml")
       with open(path, "r") as f:
          data = yaml.safe_load(f)

       return data["channels"]
    
    def get_channel(self, frequency):
       for channel in self.channels:
          if channel["frequency"] == frequency:
             return channel
          
       raise ValueError(f"No channel found for frequency {frequency} GHz")
    
    def get_frequencies(self):
       return [channel["frequency"] for channel in self.channels]
    
    def get_beam_fwhm(self, frequency):
       channel = self.get_channel(frequency)
       return channel["beam_fwhm"]
    
    def get_polarization_sensitivity(self, frequency):
       channel = self.get_channel(frequency)
       return channel["polarization_sensitivity"]