package org.enso.reference;
import org.enso.syntax.text.*;

import java.io.File;
import java.io.*;
import java.util.Scanner;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;

class Traverser {
    public static void main(String... args) throws Exception {
        Parser ps = new Parser();
        Path dir = Paths.get("std-lib");
        Path gen = Paths.get("generated");
        Files.walk(dir).forEach(path -> showFile(path, ps));
    }

    public static void showFile(Path path, Parser parser) {
        if (path.toFile().isDirectory()) {
//            System.out.println("Directory: " + file.getPath());
        } else {
            System.out.println("File: " + path);
            try {
                String content = Files.readString(path, StandardCharsets.UTF_8);

                AST.ASTOf<Shape.Module> module = parser.run(content);
                AST.ASTOf<Shape.Module> dropMeta = parser.dropMacroMeta(module);
                // Y java.lang.Error: The impossible happened.?
//                AST.ASTOf<Shape> doc  = DocParserRunner.createDocs(dropMeta);
//                String code = DocParserHTMLGenerator.generateHTMLForEveryDocumented(doc);
//                System.out.println(code);
            } catch (IOException ex) {
                System.out.println("Couldn't read file.");
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        System.out.println("Enso Reference");
        Traverser t = new Traverser();
        try {
            t.main();
        } catch (Exception e) {
            e.printStackTrace();
        }

        DocParser dp = new DocParser();
        System.out.println(dp.runMatched("*Enso* is ~cool~ superCool"));
    }
}