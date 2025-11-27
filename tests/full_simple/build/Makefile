#
# @brief   full_simple
# @version 1.0.3
# @date    2025-11-27
# @company None, free software to use 2025
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

NASM = nasm
LD   = ld
RM   = rm

include asmflags.mk
include ldflags.mk
include sources.mk
include objects.mk

EXECUTABLE=full_simple

all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(LD) $(LDFLAGS) $(OBJECTS) -o $@

%.o : %.asm
	$(NASM) $(ASMFLAGS) $< -o $@ -l $<.lst

clean:
	$(RM) -rf ../*.o *.o ../*.lst $(EXECUTABLE)
