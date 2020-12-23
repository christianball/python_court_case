class Evidence:
  def __init__(self, strength):
    self.strength = strength


class Jury:
  def reach_verdict(self, evidence_strength, lawyer_skill):
    if evidence_strength > lawyer_skill:
      print("Guilty!")
    else:
      print("Not guilty!")


class Lawyer:
  def __init__(self, name, age, skill):
    self.name = name
    self.age = age
    self.skill = skill


class Trial:
  def __init__(self, evidence, jury, lawyer):
    self.evidence = evidence
    self.jury = jury
    self.lawyer = lawyer

  def begin(self):
    # Replace the below with 1 line of code to make this trial print a verdict
    print("This trial needs programming to deliver a verdict!")


e = Evidence(10)
j = Jury()
l = Lawyer("Fisayo", 30, 10)
t = Trial(e, j, l)

t.begin()
