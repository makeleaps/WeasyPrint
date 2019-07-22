from weasyprint import HTML, CSS

to_render = """
<html><head></head><body>
<style>
table {
 width: 100%;
 border: 1px solid black;
}

td {
 border: 1px solid black;
 }
 </style>


 Yo
<table style="width: 8cm;"><tbody style="width: 8cm">

<tr>
 <td> <span>Hi</span></td>
 <td style="min-width:1cm;" >
  <span style="white-space: nowrap;">This is stuff</span>
 </td>
 <td> A test</td>
 <td style="min-width:1px;"> yo</td>
</tr></tbody>
</table>


</body></html>
"""

renderable = HTML(
    string=to_render,
)

styles = CSS(
    string="""

    """
)
renderable.write_pdf(
    target="out.pdf",
    stylesheets=[styles]
)
