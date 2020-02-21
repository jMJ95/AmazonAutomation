"""Importar paquetes de datetime, windll, UUID.
   En este archivo se encuentra la configuracion del folder
   para las descarga asi como verificar si el archivo se encuentra en dicha carpeta
"""

import datetime, time, ctypes, os, json
from ctypes import windll, wintypes
from uuid import UUID
# from PIL import Image
from io import StringIO
from io import BytesIO

# ctypes GUID copied from MSDN sample code
class GUID(ctypes.Structure):
    """
    Class of structure
    """
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", wintypes.BYTE * 8)
    ]

    def __init__(self, uuidstr):
        """
        Search the structure.
        """
        uuid = UUID(uuidstr)
        ctypes.Structure.__init__(self)
        self.Data1, self.Data2, self.Data3, \
            self.Data4[0], self.Data4[1], rest = uuid.fields
        for i in range(2, 8):
            self.Data4[i] = rest>>(8-i-1)*8 & 0xff

class Helpers:
    """Clase de utilidades para el proyecto."""

    def fullpage_screenshot(self, driver, file):
        # print("Starting chrome full page screenshot workaround ...")

        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = driver.execute_script("return document.body.clientWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        # print("Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height,viewport_width,viewport_height))
        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                # print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
                rectangles.append((ii, i, top_width,top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if not previous is None:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                # driver.execute_script("document.getElementById('topnav').setAttribute('style', 'position: absolute; top: 0px;');")
                # print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
                time.sleep(0.2)

            file_name = "part_{0}.png".format(part)
            # print("Capturing {0} ...".format(file_name))

            driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])

            # print("Adding to stitched image with offset ({0}, {1})".format(offset[0],offset[1]))
            stitched_image.paste(screenshot, offset)

            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle

        stitched_image.save(file)
        # print("Finishing chrome full page screenshot workaround...")
        return True

    def full_screenshot(self, driver, save_path):
        # initiate value
        save_path = save_path + '.png' if save_path[-4::] != '.png' else save_path
        img_li = []  # to store image fragment
        offset = 0  # where to start

        # js to get height
        height = driver.execute_script('return Math.max('
                                    'document.documentElement.clientHeight, window.innerHeight);')

        # js to get the maximum scroll height
        # Ref--> https://stackoverflow.com/questions/17688595/finding-the-maximum-scroll-position-of-a-page
        max_window_height = driver.execute_script('return Math.max('
                                                'document.body.scrollHeight, '
                                                'document.body.offsetHeight, '
                                                'document.documentElement.clientHeight, '
                                                'document.documentElement.scrollHeight, '
                                                'document.documentElement.offsetHeight);')

        # looping from top to bottom, append to img list
        # Ref--> https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
        while offset < max_window_height:

            # Scroll to height
            driver.execute_script(f'window.scrollTo(0, {offset});')
            img = Image.open(BytesIO((driver.get_screenshot_as_png())))
            img_li.append(img)
            offset += height

        # Stitch image into one
        # Set up the full screen frame
        img_frame_height = sum([img_frag.size[1] for img_frag in img_li])
        img_frame = Image.new('RGB', (img_li[0].size[0], img_frame_height))
        offset = 0
        for img_frag in img_li:
            img_frame.paste(img_frag, (0, offset))
            offset += img_frag.size[1]
        img_frame.save(save_path)

    def get_element_by_xpath(self, driver, locator):
        """Encuentra el primer elemento mediante Javascript
        utilizando como localizador un XPath.

        |Argumentos|
            - driver: instancia del WebDriver
            - locator: localizador XPath del elemento a encontrar.
        """

        script = 'return document.evaluate("' + locator + '", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;'
        return driver.execute_script(script)

    def getdatetime(self) -> str:
        """
        Retorna un string con la fecha y hora del sistema.
        """
        return datetime.datetime.utcnow().strftime('%m-%d-%Y_') + datetime.datetime.now().time().strftime('%H_%M_%S')

    shget_known_folder_path = windll.shell32.SHGetKnownFolderPath
    shget_known_folder_path.argtypes = [
        ctypes.POINTER(GUID), wintypes.DWORD,
        wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
    ]

    def _get_known_folder_path(self, uuidstr):
        """
        Obtiene la ruta del folder del usuario logeado.
        """
        pathptr = ctypes.c_wchar_p()
        guid = GUID(uuidstr)
        if self.shget_known_folder_path(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
            raise ctypes.WinError()
        return pathptr.value

    folderir_download = '{374DE290-123F-4565-9164-39C4925E467B}'

    def get_download_folder(self):
        """
        Obtiene la ruta del folder de descarga del usuario logeado.
        """
        return self._get_known_folder_path(self.folderir_download)

    def is_file_downloaded(self, file_name: str) -> bool:
        """
        Válida que un archivo se encuentra en la ruta indicada

        |Argumentos|
         - file_name: nombre del archivo a validar, por ejemplo: 'order_2820.pdf'.
        """

        i = 0

        exists = os.path.isfile(self.get_download_folder() + '\\' + file_name)

        while i <= 10 and exists == False:
            i = i + 1

            time.sleep(1)
            exists = os.path.isfile(self.get_download_folder() + '\\' + file_name)

            if exists == True:
                break

        return exists

    def eliminar_evidencias(self):
        """
        Método utilizado para eliminar los archivos con extension .png de
        la carpeta de evidencias.
        """
        path = '.\\evidencias\\'

        files = []

        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if '.png' in file:
                    files.append(os.path.join(r, file))

        for f in files:
            os.remove(f)

        print('({}) archivos eliminados de la carpeta evidencias.'.format(str(len(files))))

    def read_json_file(self, path):
        """
        Retorna un archivo de configuración.

        |Argumentos|
         - path: ruta donde se ubica el archivo.
        """

        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)