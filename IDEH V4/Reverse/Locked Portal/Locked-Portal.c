#include <stdio.h>

int check_password(char *param_1)

{
  size_t sVar1;
  int uVar2;
  
  sVar1 = strlen(param_1);
  if ((int)sVar1 == 0x19) {
    if ((((*param_1 == 'I') && (param_1[5] == 'n')) && (param_1[10] == '3')) &&
       ((param_1[0xf] == 'd' && (param_1[0x14] == 'r')))) {
      if ((((param_1[1] == 'D') && ((param_1[6] == '0' && (param_1[0xb] == '_')))) &&
          (param_1[0x10] == 'y')) && (param_1[0x15] == '_')) {
        if ((((param_1[2] == 'E') && (param_1[7] == 'w')) && (param_1[0xc] == 'r')) &&
           ((param_1[0x11] == '_' && (param_1[0x16] == 'r')))) {
          if (((param_1[3] == 'H') && ((param_1[8] == 'm' && (param_1[0xd] == '3')))) &&
             ((param_1[0x12] == 'f' && (param_1[0x17] == '3')))) {
            if ((((param_1[4] == '{') && (param_1[9] == '_')) && (param_1[0xe] == '4')) &&
               ((param_1[0x13] == '0' && (param_1[0x18] == 'v')))) {
              uVar2 = 1;
            }
            else {
              uVar2 = 0;
            }
          }
          else {
            uVar2 = 0;
          }
        }
        else {
          uVar2 = 0;
        }
      }
      else {
        uVar2 = 0;
      }
    }
    else {
      uVar2 = 0;
    }
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}

void main(void)

{
  char cVar1;
  size_t sVar2;
  char local_28 [32];
  
  printf("Enter password: ");
  fgets(local_28,0x1a,stdin);
  sVar2 = strcspn(local_28,"\n");
  local_28[sVar2] = '\0';
  cVar1 = check_password(local_28);
  if (cVar1 == '\0') {
    puts("Access denied, lol!");
  }
  else {
    puts("Access granted. Welcome to IDEH!");
  }
  return 0;
}
