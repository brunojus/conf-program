
INPUTS  := conf_html.py conf_misc.py conf_types.py make_joint_program.py
OUTPUTS := program.html program-embed.html

all: $(OUTPUTS)

clean:
	-rm $(OUTPUTS)
	-rm -r __pycache__

program.html: $(INPUTS)
	python3 make_joint_program.py --hide-people --font-size=10 -o program.html

program-embed.html: $(INPUTS)
	python3 make_joint_program.py --hide-people --font-size=9 --embeddable -o program-embed.html

sync: $(OUTPUTS) joint-program.pdf
	rsync $(OUTPUTS) joint-program.pdf fgruber@mips.complang.tuwien.ac.at:/usr/ftp/pub/hpca-cgo-ppopp-cc
