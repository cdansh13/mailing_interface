import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "C:\\Users\\erroh\\lap.py"]
    sys.exit(stcli.main())
