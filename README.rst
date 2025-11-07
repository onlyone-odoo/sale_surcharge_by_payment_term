===========
Sale Surcharge by Payment Term
===========
.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://onlyone.odoo.com/web/image/website/1/logo/OnlyOne%20Soft?unique=dccda5b
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
|badge1| |badge2| |badge3|

This module extends the functionality of payment terms to include a surcharge percentage and product, adding a surcharge line to sale orders based on the selected payment term.

**Table of contents**

.. contents::
   :local:

Configuration
=============

To configure this module, you need to:

1. Go to *Accounting > Configuration > Payment Terms*.
2. Edit or create a payment term.
3. Set the "Surcharge Percentage" and select a "Surcharge Product" (preferably a service product with appropriate taxes).

Usage
=====

1. Go to *Sales > Orders > Quotations* and create or edit a quotation.
2. Select a payment term with surcharge configured – a surcharge line will be added automatically based on the subtotal.
3. If you change to a payment term without surcharge, the line will be removed in the preview and cleaned up on save.

Known issues / Roadmap
======================

* No known issues at this time.
* Roadmap: Add support for taxes on surcharge based on customer location.

Bug Tracker
===========

Bugs are tracked on our internal issue tracker. In case of trouble, please contact us at support@onlyone.odoo.com.

Credits
=======

Authors
~~~~~~~

* Be OnlyOne

Contributors
~~~~~~~~~~~~

* `Be OnlyOne <https://onlyone.odoo.com/>`_

  * Matías Bressanello

Maintainers
~~~~~~~~~~~

This module is maintained by Be OnlyOne.