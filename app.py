"""An Nmap Scanner and Parser."""

import xmltodict
from subprocess import run
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    """Return the main page."""
    return "Nmap Scanner, a more sofisticated page is coming soon."


@app.route('/openports')
def scan_localhost():
    """Scan a host with Nmap."""
    # run nmap scan from another proccess
    target='google.com'
    run(['nmap', '-T5', '--open', '-oX', 'scan.xml', target])

    # parse Nmap XML report and covert it to a dictionary
    with open('scan.xml') as raw_xml:
        nmap_scan = xmltodict.parse(raw_xml.read())

    # Jsonify the dictionary and return it
    return jsonify(nmap_scan)


if __name__ == '__main__':
    app.run()
