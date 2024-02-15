/*
A KBase module: giannamarsContigFilter
This sample module contains one small method that filters contigs.
*/

module giannamarsContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_giannamarsContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_giannamarsContigFilter_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

    

};
