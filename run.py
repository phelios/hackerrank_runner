#!/usr/bin/env python3

import sys

from runner import Runner

args = sys.argv

package_name = args[1]
class_name = args[2]

Runner(package_name, class_name).run()