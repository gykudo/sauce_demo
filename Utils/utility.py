import re

class Utils:
  def convert_string_to_float(self, string):
    try:
      return float(re.findall("\d+\.\d+", string)[0])
    except Exception:
      return 0
