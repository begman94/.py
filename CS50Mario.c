#include <cs50.h>
#include <stdio.h>

int main(void)
{
       //int variable for height
       
       int height = get_int("Height\n");

       //bolean invalid scenarios 
      
       
       while (height < 1)
       {
              height = get_int("Height\n");
       }
       while (height > 8)
       {
              height = get_int("Height\n");
       }
       
       //bolean valid scenarios 
       
              if (height == 1)
       {
              printf("#\n");
       }
       else if (height == 2)
       {
              printf(" #\n##\n");
       }
       else if (height == 3)
       {
              printf("  #\n ##\n###\n");
       }
       else if (height == 4)
       {
              printf("   #\n  ##\n ###\n####\n");
       }
       else if (height == 5)
       {
              printf("    #\n   ##\n  ###\n ####\n#####\n");
       }
       else if (height == 6)
       {
              printf("     #\n    ##\n   ###\n  ####\n #####\n######\n");
       }
       else if (height == 7)
       {
              printf("      #\n     ##\n    ###\n   ####\n  #####\n ######\n#######\n");
       }
       else if (height == 8)
       {
              printf("       #\n      ##\n     ###\n    ####\n   #####\n  ######\n #######\n########\n");
       }
}