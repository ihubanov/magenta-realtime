# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Binary to download an asset from GCP to cache dir.

Example usage:
  python -m magenta_rt.fetch_asset --asset_path=savedmodels/test_model.model
"""

from absl import app
from absl import flags

from . import asset

_ASSET = flags.DEFINE_string(
    'asset',
    None,
    'Path to the asset to download.',
    required=True,
)
_SOURCE = flags.DEFINE_string(
    'source',
    'gcp',
    'Source to fetch the asset from.',
)
_IS_DIR = flags.DEFINE_bool(
    'is_dir',
    False,
    'Whether the asset is a directory.',
)


def main(unused_argv):
  asset.fetch(
      _ASSET.value,
      is_dir=_IS_DIR.value,
      override_cache=True,
      source=_SOURCE.value,
  )


if __name__ == '__main__':
  app.run(main)
