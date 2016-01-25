#!/usr/bin/python
import requests, sys, signal, time
print "SquidScan by Claor"
print "=================="

if len(sys.argv) < 3:
	print "Uso: ./" + sys.argv[0] + " <ip> <puerto> [archivo-puertos]"
	sys.exit()

proxy = { "http": "http://"+ sys.argv[1] +":" + sys.argv[2], }
inicio = time.time()

if len(sys.argv) == 4:
	p = open(sys.argv[3], 'r')
else:
	p = {"21","22","80","139","443","1433","3306","3389","8080"}

for n in p:
	n = n.strip()
	try: 
		r = requests.get("http://127.0.0.1:" + n, proxies=proxy, timeout=0.1)
		if r.status_code == 200:
			print "Puerto " + n + " abierto."
	except requests.exceptions.Timeout:
		pass
	except requests.exceptions.ConnectionError:
		print "Error: Target inalcanzable."
	except KeyboardInterrupt:
		sys.exit()
	print "Puerto actual: " + n + " ("+str(round(time.time() - inicio))+" seg.)"
	sys.stdout.write("\033[F\033[K")
