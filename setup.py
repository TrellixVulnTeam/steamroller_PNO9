#!/usr/bin/env python

from setuptools import setup

setup(name="SteamRoller",
      version="1.0.0",
      description="An experimental framework for text classification experiments",
      author="Tom Lippincott",
      author_email="tom@cs.jhu.edu",
      url="http://www.hltcoe.jhu.edu",
      maintainer="Tom Lippincott",
      maintainer_email="tom@cs.jhu.edu",
      packages=["steamroller",
                "steamroller.tools",
                "steamroller.tasks",
                "steamroller.models",
                "steamroller.metrics",
                "steamroller.plots",
                "steamroller.scons"],
      package_dir={"steamroller" : "src"},
      scripts=["scripts/steamroller"],
      install_requires=["concrete", "scikit-learn", "scons", "plotnine", "seaborn", "tensorflow", "valid"],
      include_package_data=True,
      #package_data={"" : ["*rst", "data/SConstruct", "data/steamroller_config.py.template"]},
     )
