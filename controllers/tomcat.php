<?php

/**
 * Apache Tomcat J2EE controller.
 *
 * @category   Apps
 * @package    Apache_Tomcat_J2EE
 * @subpackage Views
 * @author     Your name <your@e-mail>
 * @copyright  2013 Your name / Company
 * @license    Your license
 */

///////////////////////////////////////////////////////////////////////////////
// C L A S S
///////////////////////////////////////////////////////////////////////////////

/**
 * Apache Tomcat J2EE controller.
 *
 * @category   Apps
 * @package    Apache_Tomcat_J2EE
 * @subpackage Controllers
 * @author     Your name <your@e-mail>
 * @copyright  2013 Your name / Company
 * @license    Your license
 */

class Tomcat extends ClearOS_Controller
{
    /**
     * Apache Tomcat J2EE default controller.
     *
     * @return view
     */

    function index()
    {
        // Load dependencies
        //------------------

        $this->lang->load('tomcat');

        // Load views
        //-----------

        $this->page->view_form('tomcat', NULL, lang('tomcat_app_name'));
    }
}
