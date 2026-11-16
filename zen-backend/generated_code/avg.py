import java
java.io.File; 
from jnius import autoclass
JSystem = autoclass('java.lang.System')
JFile = autoclass('java.io.File');
file = JFile.open(JFile.pathToUri('Average.java'));
JSystem.out.println('The average is ' + JSystem.getProperty('line.separator') + file.readAllBytes());