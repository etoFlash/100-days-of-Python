import glob
import os
import re
from datetime import timedelta


def main():
    total_hours = 0
    for file in glob.glob(os.path.join("*-*", "README.md")):
        cur_dt = timedelta(0)
        with open(file, encoding="utf-8") as f:
            text = f.read()
            r = re.findall(r"Всего: (\d{2}):(\d{2})", text)
            counter = 0
            for h, m in r:
                counter += 1
                cur_dt += timedelta(hours=int(h), minutes=int(m))
            # doubled day 76
            if file == r"071-077\README.md":
                counter = counter - 1
            # doubled 9 days instead of 7 days
            elif file == r"092-100\README.md":
                counter = counter - 2
            assert counter == 7, f"{file} - {counter}"
        hours = cur_dt.seconds / 60 / 60
        print(f"{file} : {hours:.1f} hours")
        total_hours += hours
    print(f"Total: {total_hours:.1f} hours")


if __name__ == '__main__':
    main()
