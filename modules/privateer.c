module privateer {
  import trading;
  import random_encounters;
  import garbage_collect;
  bool garbage;
  void init (float sigdis, float detectiondis, float gendis, int minships, int genships, float fighterprob, float capprob, float garbage_collect_dist) {//negative garbage collect dist disables that feature
    random_encounters.init (sigdis, detectiondis, gendis, minships,genships,fighterprob,capprob);
    garbage=false;
    if (garbage_collect_dist>0.0) {
      garbage_collect.init (garbage_collect_dist);
      garbage=true;
    }
    trading.init();
  };
  void loop() {
    trading.loop();
    random_encounters.loop();
    if (garbage) {
      garbage_collect.loop();
    }
  };
  void initstarsystem() {
    random_encounters.initstarsystem();
  };
}
