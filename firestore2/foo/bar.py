import os
import sys

from absl import app
from absl import flags
from google.cloud import firestore


def main(argv):
  print(sys.executable)
  print(sys.version)


if __name__ == "__main__":
  app.run(main)
