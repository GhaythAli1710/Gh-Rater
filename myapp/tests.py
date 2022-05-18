from PIL.Image import Image
import io
import base64

# Create your tests here.
from myapp.models import Ghayth

with open('img.jpg', 'rb') as imagefile:
    img = imagefile.read()
    string = base64.b64encode(img)
    print(string)

# f = open('output', 'wb')
# f.write(string)
# f.close()

# b = base64.b64decode(string)
# print(b)
# img = Image.open(io.BytesIO(b))
# img.show()

# obj = Ghayth.objects.get(pk=2)
# obj = Ghayth.get_by_id(1)
# print(obj.string)
