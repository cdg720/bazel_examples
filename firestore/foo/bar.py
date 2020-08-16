import os
from google.cloud import firestore

from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string('key', None, 'key')
flags.DEFINE_string('doc_id', None, 'test')


def main(argv):
  assert FLAGS.key
  assert FLAGS.doc_id

  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = FLAGS.key

  db = firestore.Client()
  print(db.project)

  doc_ref = db.collection('debug').document(FLAGS.doc_id)
  data = {'name': 'YOUR NAME'}

  doc_ref.set(data)


if __name__ == "__main__":
  app.run(main)
