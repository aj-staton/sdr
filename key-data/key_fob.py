#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Key Fob
# Generated: Fri Sep 18 10:17:03 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class key_fob(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Key Fob")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Key Fob")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "key_fob")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.data_freq = data_freq = 315e6
        self.samp_rate = samp_rate = 0.5*data_freq

        ##################################################
        # Blocks
        ##################################################
        self.rtlsdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.rtlsdr_source_0.set_clock_source('external', 0)
        self.rtlsdr_source_0.set_time_source('gpsdo', 0)
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(data_freq, 0)
        self.rtlsdr_source_0.set_freq_corr(0, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(2, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(2, 0)
        self.rtlsdr_source_0.set_gain_mode(True, 0)
        self.rtlsdr_source_0.set_gain(6, 0)
        self.rtlsdr_source_0.set_if_gain(0, 0)
        self.rtlsdr_source_0.set_bb_gain(0, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)

        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_HAMMING, #wintype
        	315e6, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_fff(1, ([0.000231527825235,0.000234239312704,0.000236250809394,0.000237546671997,0.000238107997575,0.000237912579905,0.000236935098656,0.000235147163039,0.000232517544646,0.000229012468481,0.000224595947657,0.000219230088987,0.000212875645957,0.000205492528039,0.000197040237254,0.00018747865397,0.000176768488018,0.000164872195455,0.000151754473336,0.000137383205583,0.00012173014693,0.000104771679617,8.64897010615e-05,6.68723514536e-05,4.59148322989e-05,2.36201776715e-05,-1.81699307609e-19,-2.49247877946e-05,-5.11232901772e-05,-7.85539887147e-05,-0.000107164174551,-0.000136889400892,-0.000167653110111,-0.000199366128072,-0.000231926489505,-0.000265219248831,-0.00029911621823,-0.000333476200467,-0.000368144916138,-0.000402955134632,-0.000437727285316,-0.000472269632155,-0.000506378943101,-0.000539841304999,-0.000572432240006,-0.000603918742854,-0.000634059135336,-0.000662605161779,-0.00068930251291,-0.000713892513886,-0.000736113579478,-0.000755702785682,-0.000772397150286,-0.000785935786553,-0.000796061533038,-0.000802522758022,-0.000805075163953,-0.000803483999334,-0.00079752568854,-0.000786990160123,-0.000771682534833,-0.000751425453927,-0.000726060708985,-0.000695451453794,-0.000659483775962,-0.000618068908807,-0.000571144802961,-0.000518677639775,-0.000460663810372,-0.000397130846977,-0.000328139169142,-0.000253783073276,-0.000174191751285,-8.9530236437e-05,5.15802274534e-19,9.41605103435e-05,0.000192675579456,0.000295232137432,0.000401479919674,0.000511031714268,0.000623464118689,0.000738318136428,0.000855100341141,0.000973284244537,0.00109231157694,0.00121159409173,0.00133051571902,0.00144843477756,0.00156468641944,0.00167858507484,0.00178942736238,0.00189649546519,0.00199906039052,0.00209638522938,0.00218772841617,0.00227234931663,0.00234950892627,0.00241847732104,0.00247853551991,0.00252898084,0.00256913085468,0.00259832805023,0.00261594355106,0.00262138177641,0.00261408556253,0.00259353849106,0.00255927280523,0.00251086824574,0.00244796229526,0.00237024785019,0.00227748183534,0.00216948683374,0.00204615318216,0.00190744444262,0.00175339903217,0.00158413290046,0.00139984139241,0.00120080204215,0.000987375737168,0.000760008173529,0.000519230263308,0.000265659706201,-1.01582566529e-18,-0.000276959151961,-0.000564342597499,-0.000861190957949,-0.00116646196693,-0.00147903256584,-0.0017977009993,-0.00212119030766,-0.00244814972393,-0.00277716084383,-0.00310673983768,-0.00343534140848,-0.00376136624254,-0.00408316263929,-0.00439903559163,-0.00470724981278,-0.00500603625551,-0.00529360119253,-0.00556812994182,-0.00582779385149,-0.00607076147571,-0.00629520043731,-0.00649929000065,-0.00668122339994,-0.00683922227472,-0.00697153853253,-0.00707646459341,-0.00715234316885,-0.00719757052138,-0.00721061043441,-0.00718999560922,-0.00713433837518,-0.00704233907163,-0.00691279023886,-0.00674458453432,-0.0065367249772,-0.00628832355142,-0.00599861424416,-0.00566695583984,-0.00529283517972,-0.00487587600946,-0.00441583991051,-0.0039126300253,-0.00336629664525,-0.00277703767642,-0.00214520166628,-0.00147128861863,-0.000755952554755,1.45190432409e-18,0.000795609375928,0.00162976351567,0.00250119995326,0.0034085076768,0.00435012951493,0.0053243660368,0.00632937951013,0.00736319785938,0.00842371955514,0.00950872059911,0.010615860112,0.0117426859215,0.0128866462037,0.0140450866893,0.0152152758092,0.0163943935186,0.0175795610994,0.0187678299844,0.0199562069029,0.0211416557431,0.0223211105913,0.0234914887697,0.024649694562,0.0257926359773,0.0269172322005,0.028020426631,0.0290991924703,0.0301505569369,0.0311715919524,0.0321594402194,0.0331113226712,0.0340245440602,0.0348965004086,0.0357247069478,0.0365067720413,0.0372404493392,0.0379236079752,0.0385542698205,0.0391305945814,0.0396508947015,0.0401136465371,0.0405174978077,0.04086124897,0.0411439016461,0.0413646101952,0.0415227264166,0.0416177846491,0.0416495017707,0.0416177846491,0.0415227264166,0.0413646101952,0.0411439016461,0.04086124897,0.0405174978077,0.0401136465371,0.0396508947015,0.0391305945814,0.0385542698205,0.0379236079752,0.0372404493392,0.0365067720413,0.0357247069478,0.0348965004086,0.0340245440602,0.0331113226712,0.0321594402194,0.0311715919524,0.0301505569369,0.0290991924703,0.028020426631,0.0269172322005,0.0257926359773,0.024649694562,0.0234914887697,0.0223211105913,0.0211416557431,0.0199562069029,0.0187678299844,0.0175795610994,0.0163943935186,0.0152152758092,0.0140450866893,0.0128866462037,0.0117426859215,0.010615860112,0.00950872059911,0.00842371955514,0.00736319785938,0.00632937951013,0.0053243660368,0.00435012951493,0.0034085076768,0.00250119995326,0.00162976351567,0.000795609375928,1.45190432409e-18,-0.000755952554755,-0.00147128861863,-0.00214520166628,-0.00277703767642,-0.00336629664525,-0.0039126300253,-0.00441583991051,-0.00487587600946,-0.00529283517972,-0.00566695583984,-0.00599861424416,-0.00628832355142,-0.0065367249772,-0.00674458453432,-0.00691279023886,-0.00704233907163,-0.00713433837518,-0.00718999560922,-0.00721061043441,-0.00719757052138,-0.00715234316885,-0.00707646459341,-0.00697153853253,-0.00683922227472,-0.00668122339994,-0.00649929000065,-0.00629520043731,-0.00607076147571,-0.00582779385149,-0.00556812994182,-0.00529360119253,-0.00500603625551,-0.00470724981278,-0.00439903559163,-0.00408316263929,-0.00376136624254,-0.00343534140848,-0.00310673983768,-0.00277716084383,-0.00244814972393,-0.00212119030766,-0.0017977009993,-0.00147903256584,-0.00116646196693,-0.000861190957949,-0.000564342597499,-0.000276959151961,-1.01582566529e-18,0.000265659706201,0.000519230263308,0.000760008173529,0.000987375737168,0.00120080204215,0.00139984139241,0.00158413290046,0.00175339903217,0.00190744444262,0.00204615318216,0.00216948683374,0.00227748183534,0.00237024785019,0.00244796229526,0.00251086824574,0.00255927280523,0.00259353849106,0.00261408556253,0.00262138177641,0.00261594355106,0.00259832805023,0.00256913085468,0.00252898084,0.00247853551991,0.00241847732104,0.00234950892627,0.00227234931663,0.00218772841617,0.00209638522938,0.00199906039052,0.00189649546519,0.00178942736238,0.00167858507484,0.00156468641944,0.00144843477756,0.00133051571902,0.00121159409173,0.00109231157694,0.000973284244537,0.000855100341141,0.000738318136428,0.000623464118689,0.000511031714268,0.000401479919674,0.000295232137432,0.000192675579456,9.41605103435e-05,5.15802274534e-19,-8.9530236437e-05,-0.000174191751285,-0.000253783073276,-0.000328139169142,-0.000397130846977,-0.000460663810372,-0.000518677639775,-0.000571144802961,-0.000618068908807,-0.000659483775962,-0.000695451453794,-0.000726060708985,-0.000751425453927,-0.000771682534833,-0.000786990160123,-0.00079752568854,-0.000803483999334,-0.000805075163953,-0.000802522758022,-0.000796061533038,-0.000785935786553,-0.000772397150286,-0.000755702785682,-0.000736113579478,-0.000713892513886,-0.00068930251291,-0.000662605161779,-0.000634059135336,-0.000603918742854,-0.000572432240006,-0.000539841304999,-0.000506378943101,-0.000472269632155,-0.000437727285316,-0.000402955134632,-0.000368144916138,-0.000333476200467,-0.00029911621823,-0.000265219248831,-0.000231926489505,-0.000199366128072,-0.000167653110111,-0.000136889400892,-0.000107164174551,-7.85539887147e-05,-5.11232901772e-05,-2.49247877946e-05,-1.81699307609e-19,2.36201776715e-05,4.59148322989e-05,6.68723514536e-05,8.64897010615e-05,0.000104771679617,0.00012173014693,0.000137383205583,0.000151754473336,0.000164872195455,0.000176768488018,0.00018747865397,0.000197040237254,0.000205492528039,0.000212875645957,0.000219230088987,0.000224595947657,0.000229012468481,0.000232517544646,0.000235147163039,0.000236935098656,0.000237912579905,0.000238107997575,0.000237546671997,0.000236250809394,0.000234239312704,0.000231527825235]))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_threshold_ff_0 = blocks.threshold_ff(-2, 2, 0)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(6)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "key_fob")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_data_freq(self):
        return self.data_freq

    def set_data_freq(self, data_freq):
        self.data_freq = data_freq
        self.set_samp_rate(0.5*self.data_freq)
        self.rtlsdr_source_0.set_center_freq(self.data_freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(315e6, self.samp_rate)


def main(top_block_cls=key_fob, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
