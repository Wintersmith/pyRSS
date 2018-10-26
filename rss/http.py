
from urllib.parse import urlparse

httpScheme = 'http'
httpsScheme = 'https'

def queryStringToDict( queryString: str ) -> dict:
    retDict = {}
    
    for indivParam in queryString.split( '?' ):
        qsKey, qsValue = indivParam.split( '=' )
        retDict[ qsKey ] = qsValue
    
    return retDict
    
class URL( object ):

    def __init__( self, url ):
        self._url = url
        
    def isHTTP( self ) -> bool:
        return self._url.startswith( '{}://'.format( httpScheme )
        
    def isHTTPS( self ) -> bool:
        return self._url.startswith( '{}://'.format( httpsScheme )
        
    def getAbsolute( self ) -> str:
        return ''.join( urlparse( self._url )[ 1: ] )