
<?xml version="1.0"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
<html>
<body>
<h2>Inventory Test</h2>
<table border="1">
<tr><th>ID</th><th>Name</th><th>Quantity</th><th>Price</th></tr>
<xsl:for-each select="Inventory/product">
<tr>
<td><xsl:value-of select="id"/></td>
<td><xsl:value-of select="name"/></td>
<td><xsl:value-of select="quantity"/></td>
<td><xsl:value-of select="price"/></td>
</tr>
</xsl:for-each>
</table>
</body>
</html>
</xsl:template>

</xsl:stylesheet>
