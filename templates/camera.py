
# -*- coding: utf-8 -*-
#
# -----------------------------------------------------------------------------
# camera.py - Alpaca API responders for camera
#
# Author:   Your R. Name <your@email.org> (abc)
#
# -----------------------------------------------------------------------------
# Edit History:
#   Generated by Python Interface Generator for AlpycaDevice
#
# ??-???-????   abc Initial edit

from falcon import Request, Response, HTTPBadRequest, before
from logging import Logger
from shr import PropertyResponse, MethodResponse, PreProcessRequest, \
                get_request_field, to_bool
from exceptions import *        # Nothing but exception classes

logger: Logger = None

@before(PreProcessRequest())
class bayeroffsetx:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class bayeroffsety:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class binx:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class biny:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class camerastate:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class cameraxsize:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class cameraysize:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class canabortexposure:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class canasymmetricbin:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class canfastreadout:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class cangetcoolerpower:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class canpulseguide:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class cansetccdtemperature:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class canstopexposure:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class ccdtemperature:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class cooleron:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class coolerpower:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class electronsperadu:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class exposuremax:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class exposuremin:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class exposureresolution:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class fastreadout:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class fullwellcapacity:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class gain:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class gainmax:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class gainmin:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class gains:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class hasshutter:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class heatsinktemperature:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class imagearray:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class imagearrayvariant:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class imageready:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class ispulseguiding:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class lastexposureduration:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class lastexposurestarttime:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class maxadu:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class maxbinx:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class maxbiny:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class numx:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class numy:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class offset:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class offsetmax:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class offsetmin:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class offsets:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class percentcompleted:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class pixelsizex:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class pixelsizey:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class readoutmode:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class readoutmodes:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class sensorname:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class sensortype:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class setccdtemperature:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class startx:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class starty:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class subexposureduration:

    def on_get(self, req: Request, resp: Response, devnum: int):
        try:
            # ----------------------
            val = ## GET PROPERTY ##
            # ----------------------
            resp.text = PropertyResponse(val, req).json
        except Exception as ex:
            resp.text = PropertyResponse(None, req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class abortexposure:

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class pulseguide:

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class startexposure:

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json

@before(PreProcessRequest())
class stopexposure:

    def on_put(self, req: Request, resp: Response, devnum: int):
        formdata = req.get_media()
        ##PARAMVAL## = ##PARAMCVT##formdata['##PARAMNAME##'])
        try:
            # -----------------------------
            ### DEVICE OPERATION(PARAM) ###
            # -----------------------------
            resp.text = MethodResponse(req).json
        except Exception as ex:
            resp.text = MethodResponse(req,
                            DriverException(0x500, f'{self.__class__.__name__} failed', ex)).json
