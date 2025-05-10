#include <stdio.h>
#include <string.h>

int main() {
        char input[64];
        printf("Enter the password: ");
        scanf("%63s", input);

        if(strcmp(input, "NITO{r3v3rs3_m3}") == 0) {
                printf("Correct!\n");
        } else {
                printf("Wrong!\n");
        }

        return 0;
}

