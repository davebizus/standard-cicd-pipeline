#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from jenkinsctl.interfaces.jenkinscmd import cli

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    cli()
