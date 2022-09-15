import dpkt
import socket
import pygeoip

gl = pygeoip.GeoIP('Geocity\GeoLiteCity.dat')

def KML_builder(dstip, srcip):
    dst = gl.record_by_name(dstip)
    src = gl.record_by_name('118.179.118.225')  # Need a public key
    try:
        dstlongitude = dst['longitude']
        dstlatitude = dst['latitude']
        srclongitude = src['longitude']
        srclatitude = src['latitude']

        kml = (
        '<Placemark>\n'
        '<name>%s</name>\n'
        '<extrude>1</extrude>\n'
        '<tessellate>1</tessellate>\n'
        '<styleUrl>#transBluePoly</styleUrl>\n'
        '<LineString>\n'
        '<coordinates>%6f,%6f\n%6f,%6f</coordinates>\n'
        '</LineString>\n'
        '</Placemark>\n'
        ) %(dstip, dstlongitude, dstlatitude, srclongitude, srclatitude)
        return kml
    except:
        # print("Something is Wrong")
        return ''

def plot_ips(pcap):
    kml_packets = ''

    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            KML = KML_builder(dst, src)
            kml_packets = kml_packets + KML
        except:
            # print("Something is Wrong")
            pass
    return kml_packets

def controller():
    file = open('PCAP Files//whole.pcap', 'rb')
    pcap = dpkt.pcap.Reader(file)
    kml_header = '<?xml version="1.0" encoding="UTF-8"?> \n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'\
        '<Style id="transBluePoly">' \
        '<LineStyle>' \
        '<width>1.5</width>' \
        '<color>501400E6</color>' \
        '</LineStyle>' \
        '</Style>'
    kml_footer = '</Document>\n</kml>\n'
    kml_doc = kml_header + plot_ips(pcap) + kml_footer
    print(kml_doc)

if __name__ == "__main__":
    controller()