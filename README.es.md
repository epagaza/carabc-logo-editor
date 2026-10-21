# Carabc Logo Editor v1.0.0 — Community Edition

**Creado por Eduardo Pagaza** · Copyright © 2026 Eduardo Pagaza

Editor HTML gratuito, completamente **offline**, que sustituye únicamente el **logotipo estático de arranque** en firmwares Allwinner IMAGEWTY compatibles. Nunca sobrescribe el firmware original ni instala archivos en la pantalla.

**Idiomas:** inglés inicialmente, con español y chino simplificado. **Temas:** Dark predeterminado y Light opcional. El navegador puede recordar las preferencias.

## Cómo utilizarlo

1. Extrae el ZIP y abre `Carabc_Logo_Editor_v1.0.0.html` en Chrome o Edge actualizado. No necesitas internet.
2. En **Firmware original**, carga el `.img` sin modificar suministrado para el **modelo y revisión de hardware exactos** de tu equipo.
3. En **Editar logotipo**, selecciona JPG, PNG, BMP o WebP; ajusta proporciones, escala 10–200%, alineación, desplazamientos X/Y y fondo de color sólido, degradado o imagen. Los píxeles transparentes se fusionan con el fondo para obtener un JPEG opaco.
4. Pulsa **Previsualizar resultado** y revisa el JPEG codificado real. Si cambias la composición, vuelve a previsualizar antes de guardar.
5. En **Revisar y guardar**, acepta las advertencias. Escoge el nombre del `.img` una sola vez, mediante **Guardar como** cuando el navegador lo permita o mediante el diálogo propio del editor.
6. Utiliza **Verificar firmware** para comparar el `.img` generado con el original y guardar un reporte.
7. Lee **Siguientes pasos** para las precauciones de respaldo y compatibilidad. La instalación se realiza fuera del editor, según instrucciones específicas del fabricante.

**Sobre los fondos:** no se puede quitar automáticamente el fondo de una fotografía JPG opaca. Si quieres cambiar el fondo detrás de un logotipo negro, utiliza un PNG realmente transparente. La imagen generada debe respetar la capacidad y el perfil JPEG del firmware.

## Seguridad y compatibilidad

El editor reconoce estructuras conocidas `IMAGEWTY 0x300` y `0x403`, pero **identificar un archivo no garantiza que arranque en un dispositivo**. Solo puede cambiar la imagen de arranque, su longitud y el checksum asociado. Un caso reportado por el propietario funcionó en un Carabc HW601/DB601 V1.49, variante `txw38S0-nogps`; ello no certifica otras variantes.

**No instales un firmware sin confirmar el modelo exacto.** Conserva el original y verifica el personalizado. Consulta [Compatibilidad conocida](KNOWN_COMPATIBILITY.md) y [Seguridad y limitaciones](SAFETY_AND_COMPATIBILITY.md).

Incluye aplicación HTML, documentación, `LICENSE` (MIT), `tools/verify_imagewty.py` (verificador Python 3 de solo lectura), `TEST_REPORT_v1.0.0.md` y `CHANGELOG.md`.

**Proyecto comunitario independiente, sin afiliación, respaldo ni soporte oficial de Carabc, Allwinner, BMW o sus respectivos fabricantes.** No se distribuyen firmwares, imágenes de marcas, controladores ni programas de instalación de terceros.
