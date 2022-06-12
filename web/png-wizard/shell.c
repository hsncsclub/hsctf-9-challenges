#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/resource.h>
#include <sys/time.h>
#include <unistd.h>
int main(int argc, char** argv) {
	struct rlimit lim;
	lim.rlim_cur = lim.rlim_max = 256 * 1024 * 1024;
	if (setrlimit(RLIMIT_AS, &lim) == -1) {
		perror("setrlimit failed");
	}
	lim.rlim_cur = lim.rlim_max = 3;
	if (setrlimit(RLIMIT_CPU, &lim) == -1) {
		perror("setrlimit failed");
	}
	lim.rlim_cur = lim.rlim_max = 10 * 1024 * 1024;
	if (setrlimit(RLIMIT_FSIZE, &lim) == -1) {
		perror("setrlimit failed");
	}
	lim.rlim_cur = lim.rlim_max = 64;
	if (setrlimit(RLIMIT_NOFILE, &lim) == -1) {
		perror("setrlimit failed");
	}

	char* const args[] = {"sudo", "-S", "-u", "sub", "bash", "-c", argv[2], NULL};
	char* const envp[] = {NULL};
	execv("/usr/bin/sudo", args);
}