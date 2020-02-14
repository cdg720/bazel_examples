import os
from google.cloud import firestore

from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string('key', None, 'key')
flags.DEFINE_string('project', None, 'project')
flags.DEFINE_string('test', None, 'test')


def main(argv):
  os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = FLAGS.key

  db = firestore.Client(project=FLAGS.project)
  doc_ref = db.collection('debug').document(FLAGS.test)
  data = {'id': doc_ref.id, 'name': doc_ref.id}

  doc_ref.set(data)


if __name__ == "__main__":
  app.run(main)
