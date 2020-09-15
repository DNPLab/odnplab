import base64

from dnplab.dnpHydration import Parameter, HydrationResults


class ProcParameter(Parameter):
    """Processing Parameters

    Attributes:
        eic (float): enhancement data integration window center
        eiw (float): enhancement data integration window width
        tic (float): T1 data integration window center
        tiw (float): T1 data integration window width
        verbose (bool): Whether verbose.

    """
    def __init__(self, *args, **kwargs):  # TODO: enable manual adjustment
        super().__init__(*args, **kwargs)
        eic = 0
        eiw = 100
        tic = 0
        tiw = 100
        self.eic, self.eiw, self.tic, self.tiw = eic, eiw, tic, tiw
        self.verbose = True


def dict_to_str(mydict):
    mylist = [f"{k} \t {v}" for k, v in mydict.items()]
    return '\n'.join(mylist)


def get_table_download_link(temp_file_path, filename='results'):
    """Generates a link allowing a temp_file_path to be downloaded

    Args:
        temp_file_path(str): A string to write to a txt file and download.
        filename(str): the txt file name to generate.

    """
    b64 = base64.b64encode(temp_file_path.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.txt">Download Results</a>'
    return href


def fake_results():
    """Fake Hydration Results for Debugging"""
    # return {
    #     "uncorrected_xi":0.07918751995384089,
    #     "ksigma":35.38496657210169,
    #     "ksigma_stdd":0.4148847083010071,
    #     "ksigma_bulk_ratio":0.37091159928827766,
    #     "krho":550.3838719613336,
    #     "krho_bulk_ratio":1.5573963552952284,
    #     "klow":834.7415312673188,
    #     "klow_bulk_ratio":2.28071456630415,
    #     "coupling_factor":0.0642914307172642,
    #     "tcorr":256.5797835424664,
    #     "tcorr_bulk_ratio":4.751477473008636,
    #     "Dlocal":5.703489105008904e-10,
    #     "T10":1.4810603425640343,
    #     "T10_std":0.03748709728977797,
    #     "uncorrected_Ep":[0.1245, -3.9431, -4.1011, -7.0669, -9.1195, -10.9682, -11.7075, -11.8283, -12.6209, -13.1881, -13.8892, -14.4318, -15.3084, -15.7637, -15.7865, -15.9827, -16.3934, -17.0086, -17.3408, -17.7222, -17.9977],
    #     "interpolated_T1":[1.4207, 1.4413, 1.4423, 1.4655, 1.4884, 1.5170, 1.5316, 1.5341, 1.5529, 1.5686, 1.5909, 1.6110, 1.6495, 1.6727, 1.6739, 1.6844, 1.7072, 1.7392, 1.7507, 1.7494, 1.7286],
    #     "ksigma_array":[3.1461, 12.7840, 13.0381, 17.8512, 20.8843, 23.4711, 24.6337, 24.6501, 25.9224, 26.6498, 27.5560, 28.2268, 29.2635, 29.8960, 30.0239, 30.2758, 30.8739, 31.6965, 32.4491, 33.7103, 35.0907],
    #     "ksigma_fit":[2.2954, 11.6272, 11.9512, 17.5860, 21.0483, 23.9054, 24.9854, 25.1587, 26.2741, 27.0501, 27.9847, 28.6898, 29.7976, 30.3580, 30.3858, 30.6240, 31.1169, 31.8408, 32.2247, 32.6595, 32.9698],
    #     "E":[-0.4710, -5.0641, -5.1889, -7.6097, -9.2298, -10.7179, -11.4164, -11.4457, -12.2484, -12.7572, -13.4280, -13.9659, -14.8864, -15.4571, -15.5394, -15.7836, -16.3466, -17.1428, -17.6963, -18.4079, -18.9627],
    #     "E_power":[0.0006, 0.0043, 0.0045, 0.0087, 0.0129, 0.0183, 0.0211, 0.0216, 0.0253, 0.0285, 0.0332, 0.0376, 0.0469, 0.0531, 0.0534, 0.0565, 0.0641, 0.0789, 0.0896, 0.1053, 0.1199],
    #     "T1_std":[0.1627, 0.0126, 0.0036, 0.0082, 0.0094],
    #     "T1":[1.4000, 1.5963, 1.6559, 1.7192, 1.7575],
    #     "T1_power":[0.0006, 0.0239, 0.0534, 0.0845, 0.1132]
    # }
    return {
        "T10": None,
        "T10_std": None,
        "E": [],
        "E_power": [],
        "T1": [],
        "T1_power": []
    }
