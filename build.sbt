ThisBuild / organization := "org.enso"
ThisBuild / scalaVersion := "2.13.5"

lazy val main = (project in file("."))
  .settings(
    name := "reference",
    unmanagedBase := baseDirectory.value / "jars",
    libraryDependencies += "org.enso" % "syntax" % "0.1" from "file:///Users/maciej/NewByteOrder/reference-java/jars/parser-assembly.jar"
  )
