#
# @brief   latest
# @version 1.0.0
# @date    2024-06-19
# @company None, free software to use 2024
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

NASM = nasm
LD   = ld
RM   = rm

include asmflags.mk
include ldflags.mk
include sources.mk
include objects.mk

EXECUTABLE=latest

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(LD) $(LDFLAGS) $(OBJECTS) -o $@

%.o : %.asm
	$(NASM) $(ASMFLAGS) $< -o $@ -l $<.lst

clean:
	$(RM) -rf ../*.o *.o ../*.lst $(EXECUTABLE)
