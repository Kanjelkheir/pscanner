from scanner import utils
from scanner import scanner

def main():
    # read the arguments
    host, first_port, second_port = utils.return_args()

    # collect ports into a list
    ports_to_scan = list(range(first_port, second_port))

    # scan a set of ports using multithreading
    scanner.threaded_scan(host, ports_to_scan)



if __name__ == "__main__":
    main()
