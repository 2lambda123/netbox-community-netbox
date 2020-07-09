from dcim.models import Manufacturer
from ruamel.yaml import YAML
from pathlib import Path
import sys

file = Path('/opt/netbox/initializers/manufacturers.yml')
if not file.is_file():
  sys.exit()

with file.open('r') as stream:
  yaml = YAML(typ='safe')
  manufacturers = yaml.load(stream)

  if manufacturers is not None:
    for params in manufacturers:
      manufacturer, created = Manufacturer.objects.update_or_create(name=params['name'], defaults=params)

      if created:
        print("🏭 Created Manufacturer", manufacturer.name)
