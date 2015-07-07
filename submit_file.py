__author__ = 'bwolfson'

import sys
import optparse
import detonation_api

def build_cli_parser():
    parser = optparse.OptionParser(usage="%prog [options]", description="Submit a file for detonation to the server")

    # for each supported output type, add an option
    #
    parser.add_option("-c", "--cburl", action="store", default=None, dest="server_url",
                      help="CB server's URL.  e.g., http://127.0.0.1 ")
    parser.add_option("-f", "--filename", action = "store", default = None, dest = "filename",
                      help = "Name of the file to be uploaded")
    return parser

def main(argv):
    parser = build_cli_parser()
    opts, args = parser.parse_args(argv)
    if not opts.server_url or not opts.filename:
        print "Missing required param; run with --help for usage"
        sys.exit(-1)

    # build a detonation api object
    #
    det = detonation_api.DetApi(opts.server_url)

    file = det.submit_file(opts.filename)
    print file

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))