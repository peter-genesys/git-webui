#!/bin/sh

# Copyright 2015 Eric ALBER
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

cd $HOME
echo "Removing \$HOME/.git-webui"
rm -rf .git-webui > /dev/null 2>&1
echo "Cleaning up global gitconfig file"
git config --global --unset-all alias.webui
git config --global --remove-section webui
