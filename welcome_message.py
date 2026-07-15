import time
import random
import datetime

STRENGTH_TABLE = {
  'name':     (10, 'very common'),
  'surname':  (20, 'shared by family'),
  'nickname': (30, 'given by others'),
  'aka':      (50, 'known to few'),
}

GRADES = [
  (130, 'S', 'Legendary'),
  (100, 'A', 'Strong'),
  (70,  'B', 'Moderate'),
  (40,  'C', 'Weak'),
  (10,  'D', 'Fragile'),
  (0,   'F', 'No identity'),
]


def check_auspicious():
  today = datetime.date.today()
  total = sum(int(d) for d in str(today.year) + str(today.month).zfill(2) + str(today.day).zfill(2))
  while total > 9:
    total = sum(int(d) for d in str(total))
  return today, total, total in {1, 3, 6, 7, 9}


def short_form(idx, *names, **addons):
  try:
    code = ''.join(n[idx] for n in names)
    code = addons.get('prefix', '') + code + addons.get('suffix', '')
    return code
  except (TypeError, IndexError) as e:
    print(f'  Error: {e}')
    return None


def name_strength(**fields):
  return sum(STRENGTH_TABLE[k][0] for k, v in fields.items() if k in STRENGTH_TABLE and v)


def show_grade(fields, ns):
  max_score = sum(v[0] for v in STRENGTH_TABLE.values())
  print()
  for key, (pts, reason) in STRENGTH_TABLE.items():
    given = key in fields and fields[key]
    tick  = '✓' if given else '·'
    score = f'+{pts}' if given else '  '
    print(f'  {tick}  {key:<10} {score:>4} pts  ({reason})')
  print(f'  {"─" * 40}')
  print(f'     Total      {ns:>4} / {max_score} pts', end='  ')
  for threshold, letter, label in GRADES:
    if ns >= threshold:
      print(f'  Grade {letter} — {label}')
      break


def validate(sc, ns, is_auspicious):
  lo_ns, hi_ns = (10, 60) if is_auspicious else (50, 130)
  lo_sc, hi_sc = (4, 10)  if is_auspicious else (2, 5)

  print('\n  Verifying', end='', flush=True)
  for _ in range(3):
    time.sleep(0.4)
    print('.', end='', flush=True)
  print()

  t_ns = random.randint(lo_ns, hi_ns)
  t_sc = random.randint(lo_sc, hi_sc)
  print()
  time.sleep(0.5)
  if ns < t_ns:
    print(f'  ✗  Strength {ns} below required {t_ns}. Access denied.')
    return False
  elif len(sc) > t_sc:
    print(f'  ✗  Code "{sc}" too long (max {t_sc} chars). Access denied.')
    return False
  else:
    print('  ✓  Passed! You are cleared.')
    print(f'     Strength : {ns} pts  ≥  required {t_ns} pts  ✓')
    print(f'     Code     : "{sc}" ({len(sc)} chars)  ≤  max {t_sc} chars  ✓')
    return True


def run():
  today, cosmic, is_auspicious = check_auspicious()
  day_label = '✓ Auspicious' if is_auspicious else '✗ Not auspicious'

  print(f'\n=== Programmers\' Den — CAPTCHA ===')
  print('    Build your identity, celebrate name diversity, survive the cosmic CAPTCHA, and prove your name is strong enough to pass.')
  print()
  print(f'  {today.strftime("%A %d %B %Y")}  |  Cosmic #{cosmic}  |  {day_label}')
  if not is_auspicious:
    print('  ⚠  Stricter thresholds apply today.')
  print()

  # Step 1
  first    = input('First name  : ').strip()
  last     = input('Surname     : ').strip()
  prefix   = input('Prefix (optional, e.g. Dr) : ').strip()
  nickname = input('Nickname    (optional) : ').strip()
  aka      = input('Aka         (optional) : ').strip()

  # Short code
  sc = short_form(0, first, last, prefix=prefix)
  if not sc:
    return
  print(f'\n  Short code : {sc}')

  # Name strength + grade
  fields = {'name': first, 'surname': last, 'nickname': nickname, 'aka': aka}
  ns = name_strength(**fields)
  show_grade(fields, ns)

  # Validate
  print('\n--- CAPTCHA ---')
  validate(sc, ns, is_auspicious)
  print()


if __name__ == '__main__':
  run()
