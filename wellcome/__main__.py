from PIL import Image
from . import Wellcome
import argparse, os
import base64, sys
from io import BytesIO
args=argparse.ArgumentParser(prog=f"python3 -m {os.path.dirname(__file__).split('/')[-1]}", description='Wellcome Maker')
args.add_argument('--server',help='run as api', action='store_true')
args.add_argument('--pic',help='Picture: Path')
args.add_argument('--host', default='0.0.0.0', help='default: 0.0.0.0')
args.add_argument('--port', default=int(os.environ.get('PORT', 8000)), type=int,help=f'default: {os.environ.get("PORT", 8000)}')
args.add_argument('--capt',help= 'Caption: String')
args.add_argument('--out', help='output: Path')
args.add_argument('--base64', help='base64 output', action='store_true')
parser=args.parse_args()
try:
    if parser.server:
        from io import BytesIO
        from flask import Flask, request, Response
        import requests
        app = Flask(__name__)
        @app.route('/')
        def main():
            url = request.args.get('url')
            name = request.args.get('name')
            if name and url:
                try:
                    img=BytesIO()
                    Wellcome().create(BytesIO(requests.get(url).content), name).save(img, format='png')
                    r=Response(img.getvalue())
                    r.headers['Content-Type'] = 'image/png'
                    return r
                except Exception as e:
                    print(e)
                    return {}
            return {}
        app.run(host=parser.host, port=parser.port)
    elif parser.pic and parser.capt and (parser.out or parser.base64):
        x=Wellcome().create(parser.pic, parser.capt)
        if parser.base64:
            bit = BytesIO()
            x.save(bit, format='png')
            sys.stdout.write(base64.b64encode(bit.getvalue()).decode())
            sys.stdout.flush()
        else:
            x.save(parser.out)
            print(f'Saved: {parser.out}')
    else:
        os.system(f"python3 -m {os.path.dirname(__file__).split('/')[-1]} --help")
except Exception as e:
    print(e)
    os.system(f"python3 -m {os.path.dirname(__file__).split('/')[-1]} --help")