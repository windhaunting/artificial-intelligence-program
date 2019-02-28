import java.io.IOException;
import java.io.FileReader;
import java.io.FileWriter;

public class SudokuIO {
  static final int NUM_VARS = 81;
  static int vars[] = new int[NUM_VARS];
  static boolean varDomain[][] = new boolean[NUM_VARS][9];
  
  //Takes input from a file and creates a Sudoku CSP from that information
  public static void makeSudokuPuzzle(){
    try{
      FileReader file = new FileReader("puz-001.txt");
      for (int a = 0; a < NUM_VARS; a++){
        char ch;
        do{
          ch = (char)file.read();
        }while ((ch == '\n') || (ch == '\r') || (ch == ' '));
        if (ch == '-')
          vars[a] = 0;
        else{
          String  s = "" + ch;
          Integer i = new Integer(s);
          vars[a] = i.intValue();
          for (int j = 0; j < 9; j++){
            if (j == i.intValue() - 1)
              varDomain[a][j] = true;
            else
              varDomain[a][j] = false;
          }
        }
      }
     
      file.close();
    }
    catch(IOException e){System.out.println("File read error: " + e);}
  }
  
  //Outputs the Sudoku board to the console and a file
  public static void printSudoku(){
    try{
      FileWriter ofile = new FileWriter("output.txt", true);
      for (int a = 0; a < 9; a++){
        for (int b = 0; b < 9; b++){
          int c = 9*a + b;
          if (vars[c] == 0){
            System.out.print("- ");
            ofile.write("- ");
          }
          else{
            System.out.print(vars[c] + " ");
            ofile.write(vars[c] + " ");
          }
        }
        System.out.println("");
        ofile.write("\r\n");
      }
      ofile.write("\r\n");
      ofile.close();
    }
    catch(IOException e){System.out.println("File read error: " + e);}
  }
  
  public static void main(String[] args) {
    makeSudokuPuzzle();
    printSudoku();
  }
}
