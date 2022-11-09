import curses
import modules.time as get_time

date, time = get_time.get_time_date()

def main(stdscr, buffer=[""]):
    s = curses.initscr()
    s.nodelay(1)
    curses.noecho(); curses.raw()
    s.keypad(1)
    b = []
    R, C = s.getmaxyx() # get the maximum row and column as constants
    x, y, r, c = [0] * 4
    try:
      end = len(buffer)-1
      if len(buffer) > 0:
          cont = [ord(x) for x in buffer[:end]]
          # for rw in cont:
          #     b.append([ord(c) for c in rw])
          b.append(cont)
    except: b.append([])

    while True:
        s.move(0, 0)
        if r < y: y = r
        if r >= y + R: y = r - R+1
        if c < x: x = c
        if c >= x + C: x = c - C+1

        for rw in range(R):
            brw = rw + y
            for cl in range(C):
                bcl = cl + x
                try: s.addch(rw, cl, b[brw][bcl])
                except: pass
            s.clrtoeol()
            try: s.addch('\n')
            except: pass
        
        curses.curs_set(0)
        s.move(r-y, c-x)
        curses.curs_set(1)
        s.refresh(); ch = -1

        while (ch == -1): ch = s.getch()

        if ch != ((ch) & 0x1f) and ch < 128: 
            b[r].insert(c, ch)
            c += 1
        elif chr(ch) in '\n\r':
            l = b[r][c:]
            b[r] = b[r][:c]
            r += 1; c = 0
            b.insert(r, [] + l)
        elif ch in [8, 263]:
            if c: c -= 1; del b[r][c]
            elif r: l = b[r][c:];  del b[r]; r -= 1; c = len(b[r]); b[r] += l
        elif ch  == curses.KEY_LEFT:
            if c != 0: c -= 1
            elif r > 0: r -= 1; c = len(b[r])
        elif ch == curses.KEY_RIGHT:
            if c < len(b[r]): c += 1
            elif r < len(b)-1: r += 1; c = 0
        elif ch == curses.KEY_UP and r != 0: r -= 1
        elif ch == curses.KEY_DOWN and r < len(b)-1: r += 1

        rw = b[r] if r < len(b) else None
        rwlen = len(rw) if rw is not None else 0
        if c > rwlen: c = rwlen 

        if ch == (ord('q') & 0x1f): 
            if len(buffer) > 0: buffer.append(f"Created at: {date}, time: {time}") 
            return buffer
        elif ch == (ord('s') & 0x1f):
            buffer = []
            cont = ''
            for l in b: cont += ''.join([chr(c) for c in l]) + '\n'
            buffer.append(cont)

def call(string=[""]):
    res = curses.wrapper(main, buffer=string)
    return res